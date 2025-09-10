class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        # Convert each user's language list into a set for quick lookup
        user_languages = [set(l) for l in languages]

        # Step 1: Find which friendships cannot currently communicate
        need_fix = set()
        for u, v in friendships:
            u, v = u - 1, v - 1  # convert to 0-index
            if user_languages[u].isdisjoint(user_languages[v]):  # no common language
                need_fix.add(u)
                need_fix.add(v)

        if not need_fix:  # all friends already communicate
            return 0

        # Step 2: For each language, count how many "problem users" don't know it
        min_teach = float("inf")
        for lang in range(1, n + 1):  # languages are 1-indexed
            count = 0
            for user in need_fix:
                if lang not in user_languages[user]:
                    count += 1
            min_teach = min(min_teach, count)

        return min_teach