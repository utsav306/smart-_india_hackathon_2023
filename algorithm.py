class Algorithm:
    def __init__(self, session_time, likes, views_count, comment_count,daily_credits=5, user_level='beginner', video_level='beginner'):
        self.daily_credits = daily_credits
        self.likes = likes
        self.views_count = views_count
        self.comment_count = comment_count
        self.user_level = user_level
        self.video_level = video_level
        self.session_time = session_time

    def calculate_activity_score(self):
        return self.session_time * 0.55

    def calculate_progress_score(self):
        w1, w2 = 0.7, 0.3
        progress_score = w1 * self.calculate_activity_score() + w2 * self.daily_credits
        return progress_score

    def determine_user_level(self, thresholds=(50, 75)):
        progress_score = self.calculate_progress_score()
        if progress_score < thresholds[0]:
            return "beginner"
        elif thresholds[0] <= progress_score < thresholds[1]:
            return "intermediate"
        else:
            return "advanced"

    def map_user_level(self, user_level):
        level_mapping = {
            'beginner': 1,
            'intermediate': 2,
            'advanced': 3
        }
        return level_mapping.get(user_level.lower())

    def stuma_algorithm(self):
        w1, w2, w3, w4, w5, w6 = 0.18, 0.15, 0.2, 0.18, 0.14, 0.15

        mapped_user_level = self.map_user_level(self.user_level)

        # STuMa Algorithm
        if mapped_user_level is not None:
            mapping_score = (
                w1 * self.calculate_progress_score() +
                w2 * mapped_user_level +
                w3 * self.likes +
                w4 * self.views_count +
                w5 * self.comment_count +
                w6 * self.map_user_level(self.video_level)  # Adjusted this line
            )
            return mapping_score
        else:
            return None

# Example usage
# algorithm_instance = Algorithm(session_time=120,daily_credits=20, likes=200, views_count=1000, comment_count=50, user_level='beginner', video_level='beginner')
# progress_score = algorithm_instance.calculate_progress_score()
# user_level = algorithm_instance.determine_user_level()
# score = algorithm_instance.stuma_algorithm()

# print(f"User's Progress Score: {progress_score}")
# print(f"User's Level: {user_level}")
# print("Mapping Score:", score)
