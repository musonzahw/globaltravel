"""
Fix destination image names to use real images instead of placeholders
"""

import asyncio
from core.database import get_db
from models.destination import Destination
from sqlalchemy import select, update

async def fix_destination_images():
    """Update destination image names to use real images"""
    
    async for db in get_db():
        try:
            # Get all destinations
            stmt = select(Destination)
            result = await db.execute(stmt)
            destinations = result.scalars().all()
            
            print("🔧 Fixing destination images...")
            
            for dest in destinations:
                if dest.images and isinstance(dest.images, list):
                    old_images = dest.images.copy()
                    new_images = []
                    
                    for img in old_images:
                        # Map placeholder names to real image names
                        if img == "northern_lights_0.jpg":
                            new_images.append("Iceland_-_Golden_Circle_0.jpg")
                        elif img == "northern_lights_1.jpg":
                            new_images.append("Iceland_-_Golden_Circle_1.jpg")
                        elif img == "northern_lights_2.jpg":
                            new_images.append("Iceland_-_Golden_Circle_2.jpg")
                        elif img == "swiss_alps_interlaken_0.jpg":
                            new_images.append("Swiss_Alps_-_Interlaken_0.jpg")
                        elif img == "swiss_alps_interlaken_1.jpg":
                            new_images.append("Swiss_Alps_-_Interlaken_1.jpg")
                        elif img == "swiss_alps_interlaken_2.jpg":
                            new_images.append("Swiss_Alps_-_Interlaken_2.jpg")
                        elif img == "norwegian_fjords_0.jpg":
                            new_images.append("Alps_0.jpg")
                        elif img == "norwegian_fjords_1.jpg":
                            new_images.append("Alps_1.jpg")
                        elif img == "norwegian_fjords_2.jpg":
                            new_images.append("Alps_2.jpg")
                        else:
                            new_images.append(img)  # Keep original if no mapping
                    
                    if old_images != new_images:
                        # Update destination
                        update_stmt = update(Destination).where(Destination.id == dest.id).values(images=new_images)
                        await db.execute(update_stmt)
                        
                        print(f"✅ Updated {dest.name}:")
                        print(f"   Old: {old_images}")
                        print(f"   New: {new_images}")
                        print("-" * 50)
            
            await db.commit()
            print("🎉 Destination images updated successfully!")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            await db.rollback()

if __name__ == "__main__":
    asyncio.run(fix_destination_images())
