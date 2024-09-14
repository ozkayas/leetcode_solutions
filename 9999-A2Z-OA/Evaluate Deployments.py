import re
def evaluate_deployments(deployments: list[str]) -> list[str]:
    validator = re.compile(r'\{\"deployment_id\"\:\s\"d-\w{10}\"\,\s\"status\"\:\s\"(Success|Fail)\"\}')
    successes = failures = unreadable = 0
    for deployment in deployments:
        m = validator.fullmatch(deployment)
        if m and len(m.groups()) == 1:
            if m.group(1) == "Success":
                successes += 1
            elif m.group(1) == "Fail":
                failures += 1
            else:
                unreadable += 1
        else:
            unreadable += 1
    return [successes, failures, unreadable]

test1 = [
    '{"deployment_id": "d-123456abcd", "status": "Success"}',
    '{"deployment_id": "d-098765efgh", "status": "Fail"}',
]
test2 = [
    '{"deployment_id": "d-123456abcd", "status": "Success"}',
    '{"deployment_id": "d-098765efgh", "status": "aBCDE"}',
]
print(evaluate_deployments(test1))
print(evaluate_deployments(test2))
