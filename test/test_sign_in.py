from const import SignUpMessages


class TestSignInError:
    def test_successfully_sign_up(self, sign_in):
        sign_in.sign_in(email='test@test.test', password='Qwerty123$')
        assert sign_in.successfully_message == SignUpMessages.SIGN_UP_ERROR_MESSAGE
