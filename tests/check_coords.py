import asyncio
from core.database import get_db
from models.destination import Destination
from sqlalchemy import select

async def check_coordinates():
    async for db in get_db():
        stmt = select(Destination)
        result = await db.execute(stmt)
        destinations = result.scalars().all()
        
        print('📍 Destination Coordinates:')
        print('=' * 40)
        
        for dest in destinations:
            print(f'{dest.name}')
            print(f'  {dest.city}, {dest.country}')
            print(f'  Lat: {dest.latitude}, Lng: {dest.longitude}')
            
            if dest.latitude and dest.longitude:
                lat = float(dest.latitude)
                lng = float(dest.longitude)
                
                if lat == 0 and lng == 0:
                    print('  ❌ Default (0,0)')
                elif -90 <= lat <= 90 and -180 <= lng <= 180:
                    print('  ✅ Valid')
                else:
                    print('  ❌ Invalid')
            else:
                print('  ❌ No coords')
            print('-' * 20)

asyncio.run(check_coordinates())
