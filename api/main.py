import aiopg
from sanic import Sanic, response


app = Sanic()
connection = None


async def get_connection() -> aiopg.connect:
    """Get existing connection if not closed or create one"""
    global connection

    if connection is None or connection.closed:
        connection = await aiopg.connect(
            database='user',
            user='user',
            password='some-serious-password',
            host='sanic-bug-db',
        )

    return connection


@app.route('/')
async def hello(_):
    """Execute a query"""
    conn = await get_connection()
    cur = await conn.cursor()
    await cur.execute('SELECT true;')

    return response.json(True)


def run():
    """Application runner"""
    app.go_fast(host='0.0.0.0', port=7771)


if __name__ == '__main__':
    run()
