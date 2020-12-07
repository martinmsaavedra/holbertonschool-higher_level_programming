#include "lists.h"
/**
 * check_cycle - checks if it is a singly linked list or it has a
 * cycle in it
 * @list: list
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *reference = list, *nextnode = list;

	while (reference && nextnode && nextnode->next)
	{
		reference = reference->next;
		nextnode = nextnode->next->next;
		if (reference == nextnode)
			return (1);
	}
	return (0);
}
