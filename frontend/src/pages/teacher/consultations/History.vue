<script lang="ts">
export const description = "Teacher consultation history page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed } from "vue";

import AppSidebar from "@/components/sidebars/AppSidebar.vue";
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar";

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";

import { Separator } from "@/components/ui/separator";

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select";

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table";

import {
  History,
  User,
  Clock3,
  MessageSquare,
} from "lucide-vue-next";

const userRole = "Teacher";

// FILTERS
const sectionFilter = ref("");
const search = ref("");

// Dummy History Data
const history = ref([
  {
    id: 1,
    student: "Samantha Cruz",
    section: "STEM 11 - A",
    topic: "Performance Consultation",
    completedAt: "2025-02-05 10:00 AM",
    notes: "Discussed academic improvement plan",
  },
  {
    id: 2,
    student: "Elijah Montes",
    section: "STEM 11 - A",
    topic: "Attendance Issue",
    completedAt: "2025-01-28 2:30 PM",
    notes: "Provided guidance on attendance policy",
  },
  {
    id: 3,
    student: "Marjorie Tan",
    section: "HUMSS 12 - B",
    topic: "Grade Clarification",
    completedAt: "2025-01-22 11:00 AM",
    notes: "Explained grade breakdown and rubric",
  },
]);

const filteredHistory = computed(() => {
  return history.value.filter((h) => {
    const matchSection = sectionFilter.value ? h.section === sectionFilter.value : true;
    const matchSearch = search.value
      ? h.student.toLowerCase().includes(search.value.toLowerCase()) ||
        h.topic.toLowerCase().includes(search.value.toLowerCase())
      : true;

    return matchSection && matchSearch;
  });
});
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/consultations">Consultations</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>History</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Body -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="">
          <h2 class="text-2xl font-bold tracking-tight">Consultation History</h2>
          <p class="text-sm text-muted-foreground">
            Review all completed consultations with students.
          </p>
        </div>

        <!-- SUMMARY CARDS -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Total Consultations</CardTitle>
              <History class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">{{ history.length }}</p>
              <p class="text-xs text-muted-foreground">All-time completed sessions</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Most Consulted Section</CardTitle>
              <User class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">STEM 11 - A</p>
              <p class="text-xs text-muted-foreground">Based on history data</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Latest Session</CardTitle>
              <Clock3 class="h-5 w-5 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <p class="text-lg font-semibold">Feb 5, 2025</p>
              <p class="text-xs text-muted-foreground">Most recent consultation</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>Filter past consultations</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Section Filter -->
              <Select v-model="sectionFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search student or topic..." />
            </div>
          </CardContent>
        </Card>

        <!-- History Table -->
        <Card>
          <CardHeader>
            <CardTitle>Completed Consultations</CardTitle>
            <CardDescription>List of all past consultation records</CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Student</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Topic</TableHead>
                  <TableHead class="text-center">Completed At</TableHead>
                  <TableHead class="text-center">Notes</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="h in filteredHistory"
                  :key="h.id"
                  class="hover:bg-muted/50"
                >
                  <TableCell class="font-medium">{{ h.student }}</TableCell>
                  <TableCell>{{ h.section }}</TableCell>
                  <TableCell>{{ h.topic }}</TableCell>

                  <TableCell class="text-center">{{ h.completedAt }}</TableCell>

                  <TableCell class="text-center">
                    <Button variant="outline" size="sm" class="gap-1">
                      <MessageSquare class="h-4 w-4" />
                      View Notes
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
