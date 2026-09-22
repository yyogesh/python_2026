class AgeValidator:
    def __init__(self, age):
        self.age = age

    def is_age_valid(self):
        if self.age >= 18:
            return True
        else:
            return False


class VotingEligibilityService:
    def __init__(self, validator):
        self.validator = validator

    def check(self):
        result = self.validator.is_age_valid()

        if result is True:
            return "Eligible"
        else:
            return "Not Eligible"


validator = AgeValidator(25)
service = VotingEligibilityService(validator)

print(service.check())

# Keep It Simple
age = 25

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


def is_eligible(age):
    return age >= 18


print(is_eligible(25))