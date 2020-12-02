<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="https://cdn.iconscout.com/icon/free/png-256/gallery-44-267592.png"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Gallery Filter
        </h1>

        <p class="subheading font-weight-regular">
          請上傳你要濾鏡的圖片
          <br>圖片格式限制jpg/png
        </p>
        <v-file-input
          :rules="rules"
          accept="image/png, image/jpeg, image/bmp"
          placeholder="Pick an image"
          prepend-icon="mdi-camera"
          label="圖片"
        ></v-file-input>
      </v-col>

    </v-row>
    <v-row dense>
        <v-col
          cols="6"
        >
          <v-card>
            <v-img
              :src="original"
              class="white--text align-end"
              height="400px"
            >
              <v-card-title >原始圖片</v-card-title>
            </v-img>
              <v-card-text>
                <v-container fluid>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="sigma"
                        max="50"
                        min="-50"
                        thumb-label="always"
                        label="SIGMA"
                      ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="phie"
                        max="50"
                        min="-50"
                        thumb-label="always"
                        label="PHIE"
                      ></v-slider>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-slider
                          v-model="tau"
                          max="50"
                          min="-50"
                          thumb-label="always"
                          label="TAU"
                        ></v-slider>
                    </v-col>
                </v-row>
                </v-container>
                </v-card-text>
          </v-card>
        </v-col>
        <v-col
          cols="6"
        >
          <v-card>
            <v-img
              :src="final"
              class="white--text align-end"
              height="500px"
            >
              <v-card-title >運算後圖片</v-card-title>
            </v-img>
              
          </v-card>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: 'FilterGallery',

    data: () => ({
      original:'/images/Final1.jpg',
      final:'/images/Final1.jpg',
      sigma: 0,
      phie:0,
      tau:0
    }),
    methods:{
      uploadFile(){
        axios.get(`/api/interaction/pushList`)
        .then(res =>{
          console.log(res)
        })
        .catch(err =>{
          window.console.log(err)
        })
      }
      
    }
  }
</script>
