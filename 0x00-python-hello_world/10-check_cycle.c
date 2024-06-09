#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check the coode.
 * @list: list array
 * Description: checks if a singly linked list has a cycle in it
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
