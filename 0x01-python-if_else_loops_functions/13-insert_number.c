#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of list
 * @number: number to be inserted
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr_node;

	curr_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (curr_node == NULL || curr_node->n >= number)
	{
		new_node->next = curr_node;
		*head = new_node;
		return (new_node);
	}
	while (curr_node && curr_node->next && curr_node->next->n < number)
		curr_node = curr_node->next;
	new_node->next = curr_node->next;
	curr_node->next = new_node;

	return (new_node);
}
