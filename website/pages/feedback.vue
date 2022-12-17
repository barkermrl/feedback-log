<template>
  <v-row>
    <v-col>
      <!-- <h4 onclick="window.print();">Print</h4>

      <button @click="createpdf()">Create pdf</button> -->
      <v-row>
        <v-file-input
          v-model="chosenFile"
          chips
          label="Feedback log file"
          accept="application/JSON"
        ></v-file-input>
        <v-btn class="mx-5 my-5" @click.native="readFile">Overwrite</v-btn>
      </v-row>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card class="px-5">
          <v-card-title>Initial state</v-card-title>

          <v-textarea
            v-model="data.initialState.data"
            label="Data"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="data.initialState.model"
            label="Model"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="data.initialState.metrics"
            label="Metrics"
            rows="1"
            auto-grow
            required
          />
        </v-card>

        <v-card class="px-5 pb-5 my-5">
          <v-card-title>Records</v-card-title>

          <v-expansion-panels multiple>
            <v-expansion-panel v-for="(record, i) in data.records" :key="i">
              <v-expansion-panel-header
                >Record {{ i + 1 }}</v-expansion-panel-header
              >
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
                <UpdateTable :updates="record.updates" />
                <v-textarea
                  v-model="record.updateSummary"
                  label="Update summary"
                  rows="1"
                  auto-grow
                  required
                />
                <v-row>
                  <v-btn
                    color="error"
                    dark
                    class="ml-auto mb-2 mr-5"
                    @click.native="openDialog(i)"
                  >
                    Delete Record
                  </v-btn>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>

          <v-dialog v-model="dialog" max-width="600px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this record?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDialog"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-btn color="primary" dark class="mt-5" @click.native="newRecord"
            >New record</v-btn
          >
        </v-card>

        <v-card class="px-5">
          <v-card-title>Final state</v-card-title>

          <v-textarea
            v-model="data.finalState.data"
            label="Data"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="data.finalState.model"
            label="Model"
            rows="1"
            auto-grow
            required
          />
          <v-textarea
            v-model="data.finalState.metrics"
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

  data: function () {
    return {
      valid: false,
      dialog: false,
      recordIndex: -1,
      data: {
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
        records: [
          {
            prompt: '',
            sharedInformation: '',
            responseExpert: '',
            updateSummary: '',
            updates: [
              {
                what: 'what',
                where: '',
                when: '',
                why: '',
                impact: '',
              },
            ],
          },
        ],
      },
      chosenFile: null,
    }
  },

  methods: {
    newRecord() {
      this.data.records.push({})
    },

    openDialog(i) {
      this.recordIndex = i
      this.dialog = true
    },

    deleteItemConfirm() {
      this.data.records.splice(this.recordIndex, 1)
      this.closeDialog()
    },

    closeDialog() {
      this.dialog = false
    },

    readFile() {
      if (!this.chosenFile) {
        return
      }
      const reader = new FileReader()

      // Use the javascript reader object to load the contents
      // of the file in the v-model prop
      reader.readAsText(this.chosenFile)
      reader.onload = () => {
        this.data = JSON.parse(reader.result)
      }
    },

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
