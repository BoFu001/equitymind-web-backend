"""
api/routes/stream.py

WebSocket proxy — receives WebSocket from browser,
forwards to equitymind-core with Bearer token,
streams response back to browser.
"""

import json
import logging
import websockets

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from config import EQUITYMIND_CORE_URL, EQUITYMIND_CORE_KEY

logger = logging.getLogger(__name__)
router = APIRouter()


@router.websocket("/stream")
async def stream_proxy(websocket: WebSocket):
    await websocket.accept()
    logger.info("Browser connected to proxy")

    try:
        # ── Receive question from browser ──
        raw = await websocket.receive_text()
        data = json.loads(raw)

        # ── Connect to equitymind-core with Bearer token ──
        headers = {"Authorization": f"Bearer {EQUITYMIND_CORE_KEY}"}

        async with websockets.connect(
            EQUITYMIND_CORE_URL,
            additional_headers=headers
        ) as core_ws:
            logger.info("Connected to equitymind-core")

            # ── Forward browser message to core ──
            await core_ws.send(json.dumps(data))

            # ── Stream response from core back to browser ──
            async for message in core_ws:
                await websocket.send_text(message)

    except WebSocketDisconnect:
        logger.info("Browser disconnected")
    except Exception as e:
        logger.exception("Proxy error: %s", e)
        try:
            await websocket.send_text(
                json.dumps({"type": "error", "message": "Proxy error occurred."})
            )
        except Exception:
            pass
    finally:
        try:
            await websocket.close()
        except Exception:
            pass
