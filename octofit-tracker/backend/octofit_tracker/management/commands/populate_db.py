from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User(email='captain@marvel.com', name='Captain America', team=marvel),
            User(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User(email='batman@dc.com', name='Batman', team=dc),
            User(email='superman@dc.com', name='Superman', team=dc),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, calories=300, date='2025-12-01'),
            Activity(user=users[1], type='Cycling', duration=45, calories=400, date='2025-12-01'),
            Activity(user=users[3], type='Swimming', duration=60, calories=500, date='2025-12-01'),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', suggested_for='Marvel'),
            Workout(name='Squats', description='Lower body strength', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with superhero test data.'))
