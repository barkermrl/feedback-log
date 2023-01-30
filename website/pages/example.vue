<template>
  <v-row>
    <v-col>
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
export default {
  name: 'FeedbackPage',

  data: function () {
    return {
      valid: false,
      dialog: false,
      recordIndex: -1,
      data: {
        initialState: {
          data: 'User watch history of TV content(films, TV series, sports events) including time of day something was watched and the percentage of the content that was watched. User details, such as time being subscribed to the service',
          model:
            'Model trained on this data in order to provide recommendations for what to watch next. Model uses a Convolutional Neural Network architecture, based on the features described above.',
          metrics:
            'Click-through rates of top-N provided recommendations and the watch percentage of the recommended content (e.g. did the user watch what was recommended to them? How long did they watch it for?).',
        },
        finalState: {
          data: '',
          model: '',
          metrics: '',
        },
        records: [
          {
            prompt:
              'Poor performance on metrics - users were not watching the content that was recommended.',
            sharedInformation:
              'Model metrics in the form of click through rates and watch percentages, and a test interface to view what content gets recommended based on different watch histories .',
            responseExpert:
              'The evaluation metrics used were not adequate. If someone had watched what was recommended to them, but only watched the first half, this would be deemed a successful recommendation. Yet there is no indication that the user appreciated the recommendation or enjoyed the content.',
            updateSummary:
              'In order to better discern whether a particular recommendation was effective, the users of the TV service were given the ability to “Like” or “Dislike” particular content. This feedback was incorporated as a feature to the machine learning model, which tailored the machine learning model according to what the user liked and disliked. Users started to watch the recommended content more than they did previously.',
            updates: [
              {
                what: '“Likes” were added to content recommendations so a user could express whether a particular recommendation was good',
                where:
                  'Front end - add ability to give user feedback. Back end - add ability to store user feedback and feed this information to ML training pipeline.',
                when: 'After the initial model had been deployed.',
                why: 'To provide better recommendations to the user, meaning they spend less time choosing content and more time watching content.',
                impact:
                  'Increased click through rate and recommended content watched for longer, and more “Likes” on recommended content.',
              },
            ],
          },
        ],
      },
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
  },
}
</script>
