<template>
	<v-expansion-panel>
		<v-expansion-panel-header>Filters</v-expansion-panel-header>

		<v-expansion-panel-content>
			<v-container>
				<v-row>
					<v-radio-group label="Status">
					<v-radio label="Open"></v-radio>
					<v-radio label="Waitlisted"></v-radio>
					<v-radio label="Closed"></v-radio>
					</v-radio-group>

					<v-radio-group multiple label="Days">
					<v-radio label="Monday"></v-radio>
					<v-radio label="Tuesday"></v-radio>
					<v-radio label="Wednesday"></v-radio>
					<v-radio label="Thursday"></v-radio>
					<v-radio label="Friday"></v-radio>
					<v-radio label="Saturday"></v-radio>
					<v-radio label="Sunday"></v-radio>
					</v-radio-group>

					<v-col>
					<v-overflow-btn large label="Start Time"></v-overflow-btn>
					<v-overflow-btn large label="End Time"></v-overflow-btn>
					<v-overflow-btn large label="Instructor"></v-overflow-btn>
					</v-col>
				</v-row>
			</v-container>
		</v-expansion-panel-content>
	</v-expansion-panel>
</template>
