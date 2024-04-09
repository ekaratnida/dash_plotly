import asyncio
import json
import random
from quart import websocket, Quart
from confluent_kafka import Consumer

app = Quart(__name__)

c = Consumer({'bootstrap.servers':"44.222.204.15:29092",
              'group.id':'group1',
			  'auto.offset.reset':'earliest'})
              
c.subscribe(["test1"])

@app.websocket("/random_data")
async def random_data():
    #while True:
    #    output = json.dumps([random.random() for _ in range(10)])
    #    await websocket.send(output)
    #    await asyncio.sleep(1)
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                #print(str(msg.value().decode()))
                output = json.dumps(msg.value().decode())
                #print(output)
                await websocket.send(output)
                await asyncio.sleep(1)
    finally:
        # Close down consumer to commit final offsets.
        c.close()

if __name__ == "__main__":
    print("web socket")
    app.run(port=5000)