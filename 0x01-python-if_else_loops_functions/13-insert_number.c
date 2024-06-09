#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - check code
 * @head: pointer to head of list
 * @number: number to insert
 * Description: inserts a number into a sorted singly linked list
 * Return: address of new node, or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		if (number < (*head)->n)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			current = *head;
			while (current->next != NULL && current->next->n < number)
			{
				current = current->next;
			}
			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}
