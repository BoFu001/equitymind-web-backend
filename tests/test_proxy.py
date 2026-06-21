import asyncio
import json
import websockets

async def test():
    uri = "ws://localhost:8001/api/v1/stream"
    question = input("Enter your question: ")

    print(f"Connecting to proxy at {uri}...")

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({"question": question, "messages": []}))
        print(f"Question sent: {question}")
        print("-" * 60)

        async for message in ws:
            data = json.loads(message)
            event_type = data.get("type")

            if event_type == "connected":
                print(f"[connected] job_id={data.get('job_id')}")
            elif event_type == "progress":
                print(f"[progress] {data.get('message')}")
            elif event_type == "sub_progress":
                print(f"  ↳ {data.get('message')}")
            elif event_type == "token":
                print(data.get("text", ""), end="", flush=True)
            elif event_type == "done":
                print(f"\n[done] tickers={data.get('tickers')} top_intent={data.get('top_intent')} sub_intent={data.get('sub_intent')}")
                break
            elif event_type == "error":
                print(f"\n[error] {data.get('message')}")
                break

asyncio.run(test())
