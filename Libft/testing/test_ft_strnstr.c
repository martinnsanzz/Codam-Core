#include <stdio.h>
#include <bsd/string.h>
#include "../attempt_1/libft.h"

static void	run_test(const char *haystack, const char *needle, size_t len)
{
	char	*std;
	char	*ft;

	std = strnstr(haystack, needle, len);
	ft = ft_strnstr(haystack, needle, len);

	printf("haystack: \"%s\"\n", haystack);
	printf("needle:   \"%s\"\n", needle);
	printf("len:      %zu\n", len);

	printf("strnstr:    %p", (void *)std);
	if (std)
		printf(" -> \"%s\"", std);
	printf("\n");

	printf("ft_strnstr: %p", (void *)ft);
	if (ft)
		printf(" -> \"%s\"", ft);
	printf("\n");

	if (std != ft)
		printf("POINTER MISMATCH\n");

	printf("----------------------------------\n");
}

int	main(void)
{
	run_test("hello world", "hello", 11);
	run_test("hello world", "world", 11);
	run_test("hello world", "world", 5);
	run_test("hello world", "o w", 11);
	run_test("hello world", "o w", 7);

	run_test("abcdef", "cd", 6);
	run_test("abcdef", "cd", 3);
	run_test("abcdef", "gh", 6);

	run_test("aaaaaa", "aaa", 6);
	run_test("aaaaaa", "aaa", 2);

	run_test("test", "", 4);
	run_test("", "", 0);
	run_test("", "a", 1);

	run_test("short", "longneedle", 20);

	run_test("abc\0hidden", "hidden", 10);

	return (0);
}