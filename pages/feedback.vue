<template>
  <v-row>
    <v-col>
      <!-- <h4 onclick="window.print();">Print</h4>

      <button @click="createpdf()">Create pdf</button> -->

      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card class="px-5">
          <v-card-title>Initial state</v-card-title>

          <v-textarea
            v-model="initialState.data"
            label="Data"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="initialState.model"
            label="Model"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="initialState.metrics"
            label="Metrics"
            rows="1"
            auto-grow
            required
          />
        </v-card>

        <v-card class="px-5 pb-5 my-5">
          <v-card-title>Records</v-card-title>

          <v-expansion-panels multiple>
            <v-expansion-panel v-for="(record, i) in records" :key="i">
              <v-expansion-panel-header>{{
                record.name
              }}</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-textarea
                  v-model="record.prompt"
                  label="Prompt"
                  rows="1"
                  auto-grow
                  required
                />
                <v-textarea
                  v-model="record.sharedInformation"
                  label="Shared information with expert"
                  rows="1"
                  auto-grow
                  required
                />
                <v-textarea
                  v-model="record.responseExpert"
                  label="Response from expert"
                  rows="1"
                  auto-grow
                  required
                />
                <v-data-table
                  :headers="updateHeaders"
                  :items="record.updates"
                />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>

        <v-card class="px-5">
          <v-card-title>Final state</v-card-title>

          <v-textarea
            v-model="finalState.data"
            label="Data"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="finalState.model"
            label="Model"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="finalState.metrics"
            label="Metric performance"
            rows="1"
            auto-grow
            required
          />
        </v-card>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import { jsPDF } from 'jspdf'
import autoTable from 'jspdf-autotable'

export default {
  name: 'FeedbackPage',

  data() {
    return {
      valid: false,
      initialState: {
        data: '',
        model: '',
        metrics: '',
      },
      finalState: {
        data: '',
        model: '',
        metrics: '',
      },
      updateHeaders: [
        { text: 'What?', value: 'what' },
        { text: 'Where?', value: 'where' },
        { text: 'When?', value: 'when' },
        { text: 'Why?', value: 'why' },
        { text: 'Impact', value: 'impact' },
      ],
      records: [
        {
          name: 'Feedback 1',
          prompt: '',
          sharedInformation: '',
          responseExpert: '',
          updates: [{ what: 'what' }],
        },
      ],
    }
  },

  methods: {
    createpdf: function () {
      // eslint-disable-next-line new-cap
      const doc = new jsPDF()

      // From Javascript
      let finalY = doc.lastAutoTable.finalY || 10
      doc.text('From javascript arrays', 14, finalY + 15)
      autoTable(doc, {
        startY: finalY + 20,
        head: [['ID', 'Name', 'Email', 'Country', 'IP-address']],
        body: [
          ['1', 'Donna', 'dmoore0@furl.net', 'China', '211.56.242.221'],
          ['2', 'Janice', 'jhenry1@theatlantic.com', 'Ukraine', '38.36.7.199'],
          [
            '3',
            'Ruth',
            'rwells2@constantcontact.com',
            'Trinidad and Tobago',
            '19.162.133.184',
          ],
          ['4', 'Jason', 'jray3@psu.edu', 'Brazil', '10.68.11.42'],
          ['5', 'Jane', 'jstephens4@go.com', 'United States', '47.32.129.71'],
          ['6', 'Adam', 'anichols5@com.com', 'Canada', '18.186.38.37'],
        ],
      })

      finalY = doc.lastAutoTable.finalY
      doc.text('From HTML with CSS', 14, finalY + 15)
      // doc.autoTable({
      //     startY: finalY + 20,
      //     html: '.table',
      //     useCss: true,
      // })

      doc.output('dataurlnewwindow')
    },
  },
}
</script>
