import unittest
from app import create_app, db
from app.models import User, Profile

class ProfilesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_edit_profile(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        with self.client:
            self.client.post('/auth/login', data={
                'email': 'test@example.com',
                'password': 'password'
            })
            response = self.client.post('/profiles/edit', data={
                'bio': 'New bio',
                'avatar_url': 'http://example.com/avatar.jpg'
            })
            self.assertEqual(response.status_code, 200)
            profile = Profile.query.filter_by(user_id=user.id).first()
            self.assertEqual(profile.bio, 'New bio')
            self.assertEqual(profile.avatar_url, 'http://example.com/avatar.jpg')

if __name__ == '__main__':
    unittest.main()
    