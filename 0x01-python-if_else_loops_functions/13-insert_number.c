#include "lists.h"
/**
 *
 *
 *
 */
listint_t *add_node_start(int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	return (new);
}
listint_t *add_node_position(listint_t *node, int number)
{
	listint_t *new;
	new = malloc(sizeof(listint_t));
        if (!new)
                return (NULL);

	new->next = node->next;
	new->n = number;
	node->next = new;
	return (new);
}

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head;

	if (!head)
		return (NULL);

	if (aux == NULL)
		return (add_node_start(number));

	while (aux->n < number)
	{
		aux = aux->next;
	}
	if (aux->next == NULL)
		return (add_nodeint_end(&aux, number));
	else
		return (add_node_position(aux, number));
}
