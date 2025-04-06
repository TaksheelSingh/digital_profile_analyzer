def analyze_profile(data):
    github_score = data.get("github", {}).get("repos", 0) * 2
    leetcode_score = data.get("leetcode", {}).get("problems_solved", 0) * 1
    total_score = github_score + leetcode_score
    feedback = []

    if github_score < 30:
        feedback.append("Increase your GitHub contributions")
    if leetcode_score < 100:
        feedback.append("Practice more DSA problems")

    return {
        "recruiter_readiness_score": min(100, total_score),
        "feedback": feedback,
        "breakdown": {
            "GitHub Score": github_score,
            "LeetCode Score": leetcode_score
        }
    }