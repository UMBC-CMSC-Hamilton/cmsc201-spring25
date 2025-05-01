"""
What is Asymptotic Analysis/ Runtime analysis / Big-O Complexity ???

    It's the idea that we're going to calculate the amount of time that an algorithm / function
        takes to run, based on its input size.
    What is time?
        often what we're doing is counting steps not really time.
    Dont want the answer to depend on which machine is running it.

    Goal is to have a function f(n) so that it determines the number of steps required.
    Eliminate scale factors.

    Basis for the entire subject:
    Real World Time = [Random Constant] * f(n)
    Random Constant = speed of the processor, ram, hard drive, bus speed + 100 other factors
    We want to ignore that constant.

Define big-O:

f(n) is O(g(n)) when there are constants C and N_0 so that:
    f(n) <= C * g(n) for n >= N_0.

f(n) and g(n) are going to be "similar runtimes"
2n^2 and 5n^2 similar, their growth rates are similar.

2^n is similar to 2^n + n [n is so small compared to 2^n that it sort of vanishes.

We want to group functions by whether we can tell their runtimes apart.

If we say an algorithm runs in O(n^2) time, we're saying is that it runs in some quadratic time,
there is a constant, it could be 2 could be 100 it could be 3, so that T = C * n^2

3n^2 steps vs 5n^2 steps are both O(n^2)
3n^2 can lose to the 5n^2 when the steps in the 3n^2 are expensive, so maybe divisions
    if you're able to replace a division with a + and * you may actually save time.

Why do we not care about the distinction between 3n^2 and 5n^2 it's because we need to run a real
    time race to figure out which one is better.

f(n) is O(g(n)) when there are constants C and N_0 so that:
    f(n) <= C * g(n) for n >= N_0.

Ex:

    2n^2 + 3n + 1 is O(n^2)

    Need to show that 2n^2 + 3n + 1 <= C * n^2 [we get to pick this constant]
    3n <= 3n^2 ?? Is that true? Sure, seems true.
    1 <= n^2 For now also yes

    2n^2 + 3n + 1 <= 2n^2 + 3n^2 + n^2 = 6n^2 = pick C = 6

    2n^2 + 3n + 1 <= 6n^2
    n = 0
    1 <= 0, not right.
    As long as n >= 1 this will definitely work.  Guess what we pick N_0 = 1

    C = 6, N_0 = 1, if you pick this way, then it works.
    2n^2 + 3n + 1 is O(n^2)

    2^n + 7n^2 is O(2^n)

    2^n + 7n^2 <= C * 2^n ; C is needed because 7n^2 way less than 2^n its still positive so 2^n + whatever > 2^n

    7n^2 < 2^n

    Before n = 10 7n^2 is actually larger than 2^n
    n = 5 2^5 = 32, 7 * 5^2 = 7 * 25 = 175
    n = 10 2^10 = 1024, 7 * 10^2 = 700 2^n is bigger.  It will stay that way forever.

    lim to infinity of 2^n / (7n^2) = lim ln(2) 2^n / (14n) = lim ln(2)^2 2^n / 14 = infinity

    2^n >> 7n^2 most of the time, n ~= 10
"""