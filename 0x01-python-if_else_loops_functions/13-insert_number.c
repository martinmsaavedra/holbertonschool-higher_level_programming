#include "lists.h"
/**
 *
 *
 *
 */

 #include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node at a specified index
 * @head: pointer to first node
 * @number: number in the node to add
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *aux = NULL;	
	if (!head)
		return (NULL);	
	
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);	new->n = number;
	new->next = NULL;
	
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	aux = *head;
	
	if (aux->n > number)
	{
		new->next = aux;
		*head = new;
		return (new);
	}
	else
	{
		while (aux->next)
		{
			if (aux->n <= number && aux->next->n >= number)
			{
				new->next = aux->next;
				aux->next = new;
				return (new);
			}
			aux = aux->next;
		}
		aux->next = new;
	}
	return (new);
}