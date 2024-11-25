import unittest
from app import create_app, db
from app.models import User, Group, Message

class ChatTestCase(unittest.TestCase):
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

    def test_send_message(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        group = Group(name='Test Group')
        db.session.add(group)
        db.session.commit()
        with self.client:
            self.client.post('/auth/login', data={
                'email': 'test@example.com',
                'password': 'password'
            })
            response = self.client.post(f'/chat/group/{group.id}', data={
                'message': 'Hello, world!'
            })
            self.assertEqual(response.status_code, 200)
            message = Message.query.filter_by(body='Hello, world!').first()
            self.assertIsNotNone(message)

if __name__ == '__main__':
    unittest.main()
