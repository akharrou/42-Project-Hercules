#include <stdlib.h>
#include <unistd.h>

typedef struct 			s_unrolled {
	struct s_unrolled*	next;
	unsigned			count;
	int				values[8];
} 						t_unrolled;

t_unrolled* new_unrolled(void)
{
	t_unrolled  *new = malloc(sizeof(t_unrolled));
	if (!new)
		return (NULL);
	new->next = NULL;
	new->count = 0;
	return (new);
}


// No possible Leaks coming from here.
long	sum_unrolled(t_unrolled* list)
{
	long		sum;
	int			size;

	sum = 0;
	while (list != NULL)
	{
		// Get the size of the int array
		size = list->count;

		// Sum upp all values of the int array
		sum += list->values[--size];
		while (size != 0)
		    sum += list->values[--size];

		// Go to next list element
		list = list->next;
	}

	// Retunr the Sum
	return (sum);
}

void	del_unrolled(t_unrolled* list)
{
	t_unrolled	*tmp;

	while (list)
	{
		tmp = list;
		list = list->next;
		free(tmp);
	}
	list = NULL;
}

int		main(void)
{
	t_unrolled*	list;
	t_unrolled*	tmp;

	unsigned	i;
	int			val;
	long long	magic;

	i = 0;
	val = 0;
	list = NULL;
	magic = 753057078882375803;

	while (i < 42)
	{
		tmp = new_unrolled();
		if (tmp)
		{
			// Assigning value of int array at index count
			while (tmp->count < 8)
			{
				tmp->values[tmp->count] = val++;
				++tmp->count;
			}

			// Incrementing While Loop Counter
			++i;

			// If this is the first element of the list, create it
			if (!list)
				list = tmp;
			// Else append new list element to the front of the list
			else
			{
				tmp->next = list;
				list = tmp;
			}
		}
	}

	magic += sum_unrolled(list);
	write(1, &magic, 8);
	del_unrolled(list);

	return(0);
}
