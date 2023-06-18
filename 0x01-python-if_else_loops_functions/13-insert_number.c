#include "lists.h"

/**
 * insert_node - function inserts a number into a sorted singly linked list
 * @head: pointer to start of the list
 * @number: number to be stored in new node
 * Return: address of new node or Null on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t)), *current = *head;

    if (new_node != NULL)
    {
        new_node->n = number;
        if (current == NULL)
        {
            new_node->next = *head;
            *head = new_node;
        } else
        {
            while (current != NULL)
            {
                if (current->next != NULL)
                {
                    if ((current->n < number) & (number < current->next->n))
                    {
                        new_node->next = current->next;
                        current->next = new_node;
                        break;
                    }
                } else 
                {
                    new_node->next = current->next;
                    current->next = new_node;
                    break;
                }
                current = current->next;
            }
            return (new_node);
        }
    }
    free(new_node);
    return (NULL);
}
