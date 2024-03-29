#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - Function that reverses a list to a defined end point
 * @head: pointer to the start of the list
 * @ptr_end: point to end the reversed list
 * Return: pointer to new list on success else Null on failure
*/
listint_t *reverse_list(listint_t **head, listint_t *ptr_end)
{
	listint_t *current = *head, *prev = NULL, *next;

	next = current->next;
	/* Reverse the list */
	while (next->next != ptr_end)
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
		return (1);

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
		fast = reverse_list(&fast, midpoint);
		slow = slow->next;
	} else
	{
		midpoint = slow->next;
		fast = *head;
		printf("bfrev%d\n", fast->n);
		fast = reverse_list(&fast, midpoint);
		printf("afrev%d\n", fast->n);
		slow = midpoint;
	}
	while (slow != NULL && fast != NULL)
	{
		printf("s%d == f%d\n", slow->n, fast->n);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
