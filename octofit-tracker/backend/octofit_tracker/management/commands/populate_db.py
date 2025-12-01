from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=captain, type='Cycling', duration=45)
        Activity.objects.create(user=batman, type='Swimming', duration=60)
        Activity.objects.create(user=superman, type='Yoga', duration=20)

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for super strength')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
