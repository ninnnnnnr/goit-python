from aiohttp import web
import aiohttp
import asyncio


async def main(request):

    data1 = '{"viewport":{"topLeft":{"x":36.24676098881627,"y":50.059100081161326},"bottomRight":{"x":36.37803892977856,"y":49.98870155240915},"zoom":12.743084560156248},"type":"online5"}'
    async with aiohttp.ClientSession() as session:
        async with session.post('https://eta.api.2gis.ru/points/viewport', data=data1) as response:

           text = await response.json()
           list = text['devices']
           new_list = []
           for i in list:
               new_list.append(f'Тип транспорта - {i["transport_type"]}  -Номер общественного транспорта - {i["route_name"]}  -Скорость транспорта - {i["speed"]}')
           text = '\n'.join(str(new_list).split(',')).replace("[", '').replace("'", "").replace("]", '')
           return web.Response(text=text)



app = web.Application()
app.add_routes([web.get('/', main)])


if __name__ == '__main__':
    asyncio.run(main(app))
    web.run_app(app)