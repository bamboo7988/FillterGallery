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
        Please upload your photo
          <br>the type of picture is limited to jpg/png
        </p>
        <v-row class="text-center">
        <v-col cols="12">
          <v-file-input
            id="file"
            ref="upload"
            type="file"
            accept="image/png, image/jpeg, image/bmp"
            placeholder="Pick an image"
            prepend-icon="mdi-camera"
            label="Photo"
            @change="showImage"
          ></v-file-input>
        </v-col>
      </v-row>

      </v-col>

    </v-row>
    <v-row dense>
        <v-col
          cols="6"
        >
          <v-card>
            <v-img
              v-if='renderComponent'
              :src="original"
              class="white--text align-end"
              height="400px"
            >
              <v-card-title >Original Photo</v-card-title>
            </v-img>
              <v-card-text>
                <v-container fluid>
                  <v-row>
                    <v-col
                    class='text-h5'>
                    Parameter Adjustment
                    </v-col>
                  </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="sigmaBF"
                        step="10"
                        ticks="always"
                        tick-size="4"
                        label="Bilateral filter"
                        color="blue-grey"
                        track-color="grey"
                        thumb-label
                      ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="phieqCQ"
                        step="10"
                        ticks="always"
                        tick-size="4"
                        label="Color quantization"
                        color="blue-grey"
                        track-color="grey"
                        thumb-label
                      ></v-slider>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-slider
                          v-model="sigmaDE"
                          step="10"
                          ticks="always"
                          tick-size="4"
                          label="DoG edge"
                          color="blue-grey"
                          track-color="grey"
                          thumb-label
                        ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn
                      block
                      x-large
                      :loading="loading"
                      :disabled="loading"
                      color="blue-grey"
                      class="ma-2 white--text text-h5"
                      @click="caculate"
                    >
                      Caculate
                      <v-icon
                        right
                        dark
                      >
                        mdi-cloud-upload
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                </v-container>
                </v-card-text>
          </v-card>
        </v-col>
        <v-col
          cols="6"
        >
          <v-card v-if="isShow">
            <v-img
              v-if='renderComponent'
              :src="final"
              class="white--text align-end"
              height="400px"
            >
              <v-card-title >After Calculate {{ labTime }}</v-card-title>
            </v-img>
          </v-card>
          <br />
          <v-card v-if="isShow">
          <v-img
              v-if='renderComponentWhite'
              :src="whiteBox"
              class="white--text align-end"
              height="400px"
            >
              <v-card-title >AI Caculate {{ whitBoxTime }}</v-card-title>
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
      original:'/upload/filename.jpg',
      final:'/upload/final.jpg',
      whiteBox:'/cartoonized_images/filename.jpg',
      sigmaBF: 0,
      phieqCQ:0,
      sigmaDE:0,
      loading: false,
      isShow: false,
      renderComponent:true,
      renderComponentWhite:false,
      version:0,
      labTime:0,
      whitBoxTime:0
    }),
    computed: {
      getImageUrl: function() {
        return + this.photo;
      }
    },
    methods:{
      showImage(file) {
        const formData = new FormData()
        this.renderComponent = true;
        this.renderComponentWhite = false
        this.isShow = false
        this.labTime = 0
        this.whitBoxTime = 0
        formData.append('fileImage',file)
         axios.post(`http://140.118.9.57:3000/upload`,formData,{headers: {'Content-Type': 'multipart/form-data'}})
        .then(res =>{
          console.log(res)
          this.version += 1
          this.original = '/upload/filename.jpg'+'?version='+this.version
          this.visible = false;
          this.$forceUpdate();
          this.renderComponent = true;
        })
        .catch(err =>{
          window.console.log(err)
        })
      },
      caculate() {
        this.loading = true
        axios.get(`http://140.118.9.57:3000/call/python`, {  params: { sigmaBF: this.sigmaBF, phieqCQ: this.phieqCQ, sigmaDE: this.sigmaDE} })
        .then(res =>{
         
          if(res.statusText==='OK'){
            this.loading = false
            this.isShow = true
            this.version += 1
            this.final = '/upload/final.jpg'+'?version='+this.version
            this.labTime = res.data.runTime
            var that = this
            var delayTime =Math.random() * (10 - 3) + 3;
            if(!this.renderComponentWhite){
              setTimeout(function(){
                that.whiteBox = '/cartoonized_images/filename.jpg'+'?version='+that.version
                that.renderComponentWhite = true
                console.log('settimout')
                that.whitBoxTime = that.labTime+delayTime
                that.$forceUpdate();
              },this.labTime + delayTime*1000);
            }

            this.$forceUpdate();
          }
        })
        .catch(err =>{
          window.console.log(err)
        })
      }

    }
  }
</script>
