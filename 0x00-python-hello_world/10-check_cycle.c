#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *next = list;

	if (list == NULL)
		return (0);
	while (curr && next && next->next)
	{
		curr = curr->next;
		next = next->next->next;
		if (curr == next)
			return (1);
	}
	return (0);
}
