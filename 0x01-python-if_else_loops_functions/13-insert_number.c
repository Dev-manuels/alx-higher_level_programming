#include "lists.h"

/**
 * insert_node - Function thats inserts a node in a sorted linked list
 * @head: pointer to start of list
 * @number: number to be inserted at new node
 * Return: pointer to new node on success else Null
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t)), *current = NULL;

	if (head == NULL || newNode == NULL)
	{
		free(newNode);
		return (NULL);
	}
	newNode->n = number;
	current = (*head);
	if (current->n <= newNode->n)
	{
		newNode->next = current;
		*head = newNode;
	} else
	{
		while (current->next)
		{
			if (current->n <= newNode->n && newNode->n <= (current->next)->n)
			{
				newNode->next = current->next;
			}
			current = current->next;
		}
		if (newNode->next == NULL)
		{
			current->next = newNode;
		}
	}
	return (newNode);
}
