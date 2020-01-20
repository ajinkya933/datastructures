'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.

Solution:
    Given a problem always try to split it into all the cases
    for example in the above prblem we can split this problem

        First case: what happens when there is no input provided           \
                    that is input -> ""                                     \
                                                                             \
                    Here, there is only one way to represent no input         \
                    that is no input so return 1.                              \
                                                                                \      Here for both of these cases  we return 1 so in code
        Second case: what happens if only one character is provided             /      we can just mention this as a single case where input -> ""
                    that is  input -> "a"                                      /       is no string
                                                                              /
                    Here, there is only one way to represent one character   /
                    and that is the character itself                        /
                    so return 1                                            /

        Third case: what happens when input -> "1234"
                    Here, input  = num of ways to represent '1' + num of
                    ways to represent '234' + num of ways to represent '34'


        Fourth case: What happens when input -> "2713"
                     Here, input  = num of ways to represent '2' + num of
                     ways to represent "213"

                     in this case we cannot take 27 because we have all the
                     alphabets in range 0 to 26

        Fifth case: What happens when input[0] = 0


'''



def helper(data, k):
    if k == 0:
        return 1

    s=len(data) - k
    if data[s] == '0':
        return 0

    result = helper(data, k-1)
    if k>=2 and int(data[s:s+2]) <=26:
        result = result + helper(data, k-2)
    return result


def my_list(data):
    return helper(data, len(data))

a_input="111"   # "aaa", "ka", "ak"
res = my_list(a_input)
print(res)
