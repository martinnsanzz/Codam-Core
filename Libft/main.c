#include <stdio.h>
#include <string.h>
#include "attempt_1/libft.h"

static void	print_buffer(unsigned char *buf, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n)
	{
		printf("%02X ", buf[i]);
		i++;
	}
	printf("\n");
}

static void	test_basic_copy(void)
{
	char	src[] = "Hello World";
	char	dest[20];

	printf("===== BASIC STRING COPY =====\n");

	ft_memcpy(dest, src, 12);

	printf("expected: Hello World\n");
	printf("result:   %s\n\n", dest);
}

static void	test_partial_copy(void)
{
	char	src[] = "ABCDEFGHIJ";
	char	dest[20];

	printf("===== PARTIAL COPY =====\n");

	ft_memcpy(dest, src, 5);
	dest[5] = '\0';

	printf("expected: ABCDE\n");
	printf("result:   %s\n\n", dest);
}

static void	test_binary_copy(void)
{
	unsigned char	src[8] = {0, 1, 2, 3, 4, 5, 6, 7};
	unsigned char	dest[8];

	printf("===== BINARY DATA COPY =====\n");

	ft_memcpy(dest, src, 8);

	printf("expected:\n");
	print_buffer(src, 8);

	printf("result:\n");
	print_buffer(dest, 8);

	printf("\n");
}

static void	test_offset_copy(void)
{
	char	buffer[20] = "123456789";

	printf("===== POINTER OFFSET COPY =====\n");

	ft_memcpy(buffer + 5, "ABC", 3);

	printf("expected pattern: 12345ABC9\n");
	printf("result:           %s\n\n", buffer);
}

static void	test_zero_length(void)
{
	char	src[] = "HELLO";
	char	dest[20] = "XXXXXXXXXX";

	printf("===== ZERO LENGTH COPY =====\n");

	ft_memcpy(dest, src, 0);

	printf("expected: XXXXXXXXXX\n");
	printf("result:   %s\n\n", dest);
}

static void	test_large_copy(void)
{
	char	src[100];
	char	dest[100];
	size_t	i;

	printf("===== LARGE COPY =====\n");

	i = 0;
	while (i < 99)
	{
		src[i] = 'A' + (i % 26);
		i++;
	}
	src[99] = '\0';

	ft_memcpy(dest, src, 100);

	printf("expected first 20 chars: %.20s\n", src);
	printf("result   first 20 chars: %.20s\n\n", dest);
}

int	main(void)
{
	test_basic_copy();
	test_partial_copy();
	test_binary_copy();
	test_offset_copy();
	test_zero_length();
	test_large_copy();
	return (0);
}