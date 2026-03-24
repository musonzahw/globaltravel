"""
Test Stripe Payment with Mock Data
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from models.payment import Payment
from models.booking import Booking
from models.user import User
from sqlalchemy import select, and_

async def create_test_stripe_payment():
    """Create a test Stripe payment record"""
    
    async for db in get_db():
        try:
            # Find a booking for user 4 (get the first one)
            stmt = select(Booking).where(Booking.user_id == 4).limit(1)
            result = await db.execute(stmt)
            booking = result.scalar_one_or_none()
            
            if not booking:
                print("❌ No booking found for user 4")
                return
            
            # Create a test Stripe payment
            payment = Payment(
                booking_id=booking.id,
                user_id=4,
                amount=10.00,
                currency="USD",
                payment_method="stripe",
                payment_status="succeeded",
                stripe_payment_id="pi_test_1234567890",
                stripe_charge_id="ch_test_1234567890"
            )
            
            db.add(payment)
            await db.commit()
            await db.refresh(payment)
            
            print(f"✅ Created test Stripe payment:")
            print(f"   Payment ID: {payment.id}")
            print(f"   Booking ID: {payment.booking_id}")
            print(f"   Amount: ${payment.amount}")
            print(f"   Stripe Payment ID: {payment.stripe_payment_id}")
            print(f"   Status: {payment.payment_status}")
            
            return payment
            
        except Exception as e:
            print(f"❌ Error creating test payment: {e}")
            await db.rollback()

if __name__ == "__main__":
    asyncio.run(create_test_stripe_payment())
