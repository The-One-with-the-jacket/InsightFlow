import unittest
from app import create_app, db
from app.models import User, Group, Membership

class GroupsTestCase(unittest.TestCase):
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

    def test_create_group(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        with self.client:
            self.client.post('/auth/login', data={
                'email': 'test@example.com',
                'password': 'password'
            })
            response = self.client.post('/groups/create', data={
                'name': 'Test Group',
                'description': 'This is a test group',
                'private': False
            })
            self.assertEqual(response.status_code, 200)
            group = Group.query.filter_by(name='Test Group').first()
            self.assertIsNotNone(group)
            membership = Membership.query.filter_by(user_id=user.id, group_id=group.id).first()
            self.assertEqual(membership.role, 'owner')

if __name__ == '__main__':
    unittest.main()
