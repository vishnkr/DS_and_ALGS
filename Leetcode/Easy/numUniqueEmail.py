#problem: https://leetcode.com/problems/unique-email-addresses

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_dict={}
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.','')
            if '+' in local:
                local = local.replace(local[local.index('+'):],'')   
            final_email = local+'@'+domain
            if final_email in email_dict:
                email_dict[final_email]+=1
            else:
                email_dict[final_email]=1
        return len(email_dict)
            