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

	if (newNode == NULL)
	{
		free(newNode);
		return (NULL);
	}
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	current = (*head);
	if (newNode->n <= current->n)
	{
		newNode->next = current;
		*head = newNode;
	} else
	{
		while (current->next)
		{
			if ((current->next)->n >= newNode->n)
			{
				newNode->next = current->next;
				break;
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
