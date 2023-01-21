import {createStore} from 'vuex';

export default createStore({
	state: () =>  ({
		tickets: [],
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			state.tickets = tickets
		},
		setNewTicketStatusById(state, element){
			state.tickets.find((ticket) => ticket.id === element.elementId).status = element.newStatus
		},
	},
	actions: {
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		},
		async patchNewTicketStatusById(ctx, element) {
			const cookie = document.cookie
			ctx.commit('setNewTicketStatusById', element)
			await fetch(`http://127.0.0.1:8000/api/appeal/${element.elementId}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': element.newStatus
				})
			})
		},
		async patchTicketNotes(ctx, element, newNote) {
			const cookie = document.cookie
			if (element.notes !== newNote) {
				await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
					method: 'PATCH',
					headers: {
						'Content-Type': 'application/json',
						'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
					},
					body: JSON.stringify({
						'notes': newNote
					})
				})
			}
		},
		async deleteTicketById(ctx, ticketId) {
			const cookie = document.cookie
			await fetch(`http://127.0.0.1:8000/api/appeal/${ticketId}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				}
			})
		},
	}
})
