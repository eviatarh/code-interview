package com.example.vim.model


data class Provider(
    var name: String,
    val score: Float,
    var specialties: List<String>,
    val availableDates: List<AvailableDate>
)