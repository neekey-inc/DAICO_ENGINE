<template>
  <section>
    <el-button><a @click="$router.push({name:'management'})">予約管理</a></el-button>
    <el-button><a @click="$router.push({name:'setting'})">会社情報</a></el-button>
    <el-button><a @click="$router.push({name:'analysis'})">分析</a></el-button>
    <el-button><a @click="$router.push({name:'mail'})">メール</a></el-button>
  </section>
</template>
