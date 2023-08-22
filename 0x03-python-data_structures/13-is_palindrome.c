#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - Function that reverses a list to a defined end point
 * @head: pointer to the start of the list
 * @ptr_end: pointer to desired end of reversed list. Can be NULL.
 * Return: pointer to new list on success else Null on failure
*/
listint_t *reverse_list(listint_t **head, listint_t *ptr_end)
{
	listint_t *current = *head, *prev = NULL, *next;

	/* Check that head is valid */
	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		return (NULL);
	}

	/* Check if a desired node end is set */
	if (ptr_end != NULL)
		prev = ptr_end;
	/* Reverse the list */
	while (current->next != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (current);
}

/**
 * is_palindrome - Function that checks if a singly list is a palindrome
 * @head: pointer to start of list
 * Return: 0 if it is not a palindrome and 1 if it is.
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *midpoint;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (0);

	slow = *head;
	fast = *head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast->next == NULL)
	{
		midpoint = slow;
		fast = *head;
		while (fast->next != midpoint)
			fast = fast->next;
		fast = reverse_list(&fast, NULL);
		slow = slow->next;
	} else
	{
		midpoint = slow->next;
		fast = *head;
		while (fast->next != midpoint)
			fast = fast->next;
		fast = reverse_list(&fast, NULL);
		slow = slow->next;
	}
	while (slow != NULL && fast != NULL)
	{
		if (fast->n != slow->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
