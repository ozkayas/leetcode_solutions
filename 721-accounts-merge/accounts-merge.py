from collections import defaultdict, namedtuple
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        Account = namedtuple("Account", ["mail","name"])

        parent = dict()

        # Initialize each account mail as its own parent
        for account in accounts:
            for mail in account[1:]:
                acc = Account(mail, account[0])
                parent[acc] = acc

        # Find function with path compression
        def find(a: Account) -> Account:
            if parent[a] != a:
                parent[a] = find(parent[a])  # Path compression
            return parent[a]

        # Union function
        def union(a: Account, b: Account):
            parent[find(b)] = find(a)

        # Perform union operations for all mails in the same account
        for account in accounts:
            firstAccount = Account(account[1], account[0])
            for mail in account[2:]:
                acc = Account(mail, account[0])
                union(acc, firstAccount)

        # Group emails by their root account using defaultdict
        groups = defaultdict(list)
        for acc in parent:
            root = find(acc)
            groups[root].append(acc.mail)

        # Prepare the result
        result = []
        for root, emails in groups.items():
            result.append([root.name] + sorted(emails))

        return result


        