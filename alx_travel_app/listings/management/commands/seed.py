from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed the database with sample Listings, Bookings, and Reviews"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Create sample users
        users = []
        for i in range(5):
            user, _ = User.objects.get_or_create(username=f"user{i}")
            users.append(user)

        # Create sample listings
        listings = []
        for i in range(10):
            listing = Listing.objects.create(
                title=f"Listing {i}",
                description="Sample description",
                price_per_night=random.randint(50, 500),
                location=f"City {i}",
            )
            listings.append(listing)

        # Create sample bookings
        for i in range(20):
            booking = Booking.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                check_in=date.today(),
                check_out=date.today() + timedelta(days=random.randint(1, 10)),
                guests=random.randint(1, 5),
            )

        # Create sample reviews
        for i in range(15):
            Review.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                rating=random.randint(1, 5),
                comment="This is a sample review",
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
