#include "lists.h"
/**
 *is_palindrome - function in C that checks if a singly linked
 *list is a palindrome.
 *@head: double pointer to head
 *Return: 1 if palindrome 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int arr[5000];
	int m = 0, i = 0;

	if (head == NULL)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);
	for (; aux; aux = aux->next, i++)
		arr[i] = aux->n;
	for (; i > m; m++, i--)
	{
		if (arr[m] != arr[i - 1])
			return (0);
	}
	return (1);
}
