thonclass UserInfoParser:
    @staticmethod
    def parse_user_info(user_info):
        return {
            'username': user_info.get('username'),
            'location': user_info.get('location'),
            'avatar': user_info.get('avatar'),
            'profile_link': user_info.get('link')
        }