#include "lists.h"
/**
 *
 *
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux;
	
	new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);


	if (!head)
		return (NULL);

	if (*head == NULL)
	{
			
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	aux = *head;
	while (aux->next)
	{
		if (aux->n <= number && aux->next->n >= number)
		{
			new->next = aux->next;
			new->n = number;
			aux->next = new;
			
			return (new);
		}
		aux = aux->next;
	}
	aux->next = new;
	/*if (aux->next == NULL)
		return (add_nodeint_end(head, number));*/
	return (new);
}
