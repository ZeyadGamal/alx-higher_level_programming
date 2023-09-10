#include "lists.h"

listint_t *list_reverse(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * list_reverse - reverses a singly linked list
 * @head: pointer to list
 * Return: pointer to new list
 */
listint_t *list_reverse(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *next, *prev = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to linked list
 * Return: 1 if palindrome, 0 othewise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *middle, *reverse;
	int list_size = 0;
	int i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		list_size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (list_size / 2) - 1; i++)
		temp = temp->next;
	if ((list_size % 2 == 0) && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reverse = list_reverse(&temp);
	middle = reverse;
	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	list_reverse(&middle);
	return (1);
}
