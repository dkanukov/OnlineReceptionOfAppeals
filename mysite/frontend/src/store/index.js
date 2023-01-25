import {createStore} from 'vuex';

export default createStore({
	state: () => ({
		tickets: [],
		user: null,
		filterHelpType: []
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			state.tickets = tickets
		},
		setNewTicketStatusById(state, element) {
			state.tickets.find((ticket) => ticket.id === element.elementId).status = element.newStatus
		},
		setUser(state, user) {
			state.user = user
		},
		deleteTicket(state, ticketId) {
			state.tickets = state.tickets.filter((ticket) => ticket.id !== ticketId)
		}
	},
	actions: {
		async getUser(ctx) {
			const ans = await fetch('http://127.0.0.1:8000/api/user', {method: 'GET'})
			if (ans.ok) {
				const res = await ans.json()
				ctx.commit('setUser', res)
			} else {
				console.log(`Не удалось получить пользователя`)
			}

		},
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		},
		async patchTicketStatusById(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.elementId}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': element.newStatus
				})
			})
			if (res.ok) {
				ctx.commit('setNewTicketStatusById', element)
			} else {
				console.log(`Не удалось обновить статус тикета с ID: ${element.id}`)
			}
		},
		async patchTicketNotes(ctx, element, newNote) {
			const cookie = document.cookie
			if (element.notes !== newNote) {
				const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
					method: 'PATCH',
					headers: {
						'Content-Type': 'application/json',
						'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
					},
					body: JSON.stringify({
						'notes': newNote
					})
				})
				if (!res.ok) {
					console.log(`Не удалось обновить заметку тикета с ID: ${element.id}`)
				}
			}
		},
		async deleteTicketById(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
			})
			if (res.ok) {
				ctx.commit('deleteTicket', element.id)
			} else {
				console.log(`Не удалось удалить тикет ${element.id}`)
			}
		},
		async pathTicketFlag(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'flag': !element.flag
				})
			})
			if (!res.ok) {
				console.log(`Не удалось отметить тикет ${element.id}`)
			}
		}
	}
})
